import argparse
import logging
import os

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms

from unet import UNet
from utils.data_vis import plot_img_and_mask
from utils.dataset import BasicDataset


def predict_img(net,
                full_img,
                device,
                scale_factor=1,
                out_threshold=0.5):
    net.eval()

    img = torch.from_numpy(BasicDataset.preprocess(full_img, scale_factor))

    img = img.unsqueeze(0)
    img = img.to(device=device, dtype=torch.float32)

    with torch.no_grad():
        output = net(img)
        #print(output)
        #print(output.shape)
        # CHW
        # print(output[0,:,62,205])
        #print(output[0,:,92,244])
        if net.n_classes > 1:
            probs = F.softmax(output, dim=1)
        else:
            probs = torch.sigmoid(output)
        #print(probs)
        probs = probs.squeeze(0)
        # print(probs[:,62,205])
        #print(probs[:,92,244])
        tf = transforms.Compose(
            [
                transforms.ToPILImage(),
                transforms.Resize(full_img.size[1]),
                transforms.ToTensor()
            ]
        )

        probs = tf(probs.cpu())
        full_mask = probs.squeeze().cpu().numpy()
        #VPred50IR.png
        # print("Pozadie")
        # print(full_mask[:,0,0])
        # print("Vcela")
        # print(full_mask[:,113,339])
        # print("Kliestik")
        # print(full_mask[:,124,412])

        # Pozadie
        # [0.         0.         0.99607843]
        # Vcela
        # [0.         0.99607843 0.        ]
        # Kliestik
        # [0.5882353  0.40784314 0.        ]

        #VKPred27IR
        # print("Pozadie")
        # print(full_mask[:,0,0])
        # print("Vcela")
        # print(full_mask[:,161,481])
        # print("Kliestik")
        # print(full_mask[:,185,488])
        # Pozadie
        # [0.         0.         0.99607843]
        # Vcela
        # [0.00392157 0.99215686 0.        ]
        # Kliestik
        # [0.9490196  0.04705882 0.        ]
    return full_mask > out_threshold


def get_args():
    parser = argparse.ArgumentParser(description='Predict masks from input images',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model', '-m', default='MODEL.pth',
                        metavar='FILE',
                        help="Specify the file in which the model is stored")
    parser.add_argument('--input', '-i', metavar='INPUT', nargs='+',
                        help='filenames of input images', required=True)

    parser.add_argument('--output', '-o', metavar='INPUT', nargs='+',
                        help='Filenames of ouput images')
    parser.add_argument('--viz', '-v', action='store_true',
                        help="Visualize the images as they are processed",
                        default=False)
    parser.add_argument('--no-save', '-n', action='store_true',
                        help="Do not save the output masks",
                        default=False)
    parser.add_argument('--mask-threshold', '-t', type=float,
                        help="Minimum probability value to consider a mask pixel white",
                        default=0.5)
    parser.add_argument('--scale', '-s', type=float,
                        help="Scale factor for the input images",
                        default=0.5)

    return parser.parse_args()


def get_output_filenames(args):
    in_files = args.input
    out_files = []

    if not args.output:
        for f in in_files:
            pathsplit = os.path.splitext(f)
            out_files.append("{}_OUT{}".format(pathsplit[0], pathsplit[1]))
    elif len(in_files) != len(args.output):
        logging.error("Input files and output files are not of the same length")
        raise SystemExit()
    else:
        out_files = args.output

    return out_files


def mask_to_image(mask):
    # print(mask)
    mask = mask.astype(np.uint8)
    # print(mask)
    mask = mask*255
    # print(mask.shape)
    # CHW to HWC
    img_trans = mask.transpose((1, 2, 0))
    # print(img_trans.shape)
    #return Image.fromarray((mask * 255).astype(np.uint8))
    return Image.fromarray(img_trans, mode='RGB')


if __name__ == "__main__":
    ReadPath = ".\\data\\imgs"
    ReadPath = "C:\\Users\\Samuel\\OneDrive - VUT\\VUT_Brno_FEKT\\DP\\TestovaciDataset\\IR"
    dir_list = os.listdir(ReadPath)
    #for i in range(20,31):
    model = ".\\checkpoints_povodne\\CP_epoch20_final1.pth"#".\\checkpoints_povodne\\CP_epoch"+str(i)+".pth"
    #print(os.listdir(".\\checkpoints"))
    #print(dir_list)
    net = UNet(n_channels=3, n_classes=3)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net.to(device=device)
    net.load_state_dict(torch.load(model, map_location=device))
    # WP = ".\\PredPosunutySoftmax\\60\\"
    WP = ".\\TestovaciDatasetDoDP\\"
    for path in dir_list:
        RP = ReadPath + '\\' + path
        img = Image.open(RP)
        mask = predict_img(net=net,
                        full_img=img,
                        scale_factor=0.5,#args.scale,
                        out_threshold=0.5,#args.mask_threshold,
                        device=device)
        #out_fn = WP + path
        result = mask_to_image(mask)
        result.save(WP + path)
    print("Koniec")















    # args = get_args()
    # in_files = args.input
    # out_files = get_output_filenames(args)


    # net.load_state_dict(torch.load(args.model, map_location=device))

    # logging.info("Model loaded !")

    # for i, fn in enumerate(in_files):
    #     logging.info("\nPredicting image {} ...".format(fn))

    #     img = Image.open(fn)

    #     mask = predict_img(net=net,
    #                        full_img=img,
    #                        scale_factor=args.scale,
    #                        out_threshold=args.mask_threshold,
    #                        device=device)

    #     if not args.no_save:
    #         out_fn = out_files[i]
    #         result = mask_to_image(mask)
    #         result.save(out_files[i])

    #         logging.info("Mask saved to {}".format(out_files[i]))

    #     if args.viz:
    #         logging.info("Visualizing results for image {}, close to continue ...".format(fn))
    #         plot_img_and_mask(img, mask)
