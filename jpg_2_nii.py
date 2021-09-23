import os
import numpy as np

from os.path import isfile, join

import nibabel as nib
from PIL import Image

from torchvision import transforms




def getImageImageList(imagesFolder):
    if os.path.exists(imagesFolder):
       imageNames = [f for f in os.listdir(imagesFolder) if isfile(join(imagesFolder, f))]

    imageNames.sort()

    return imageNames




# Subj_181 ~~ 등 여러 폴더들 이미지들을 .nii 로 변환해주는 함수

def img_2_nifti():

    # path = '/home/has/Datasets/CT_annotated_Kidney2_only_img2'
    orgin_path = '/home/has/Datasets/Bladder_240.jpg_mask'
    # orgin_path = '/home/has/Datasets/Ureter_dataset3'
    case_list = next(os.walk(orgin_path))[1]
    case_list.sort()
    print(case_list)

    # path = os.path.join(orgin_path, case_list[0])
    # print(path)



    for case in case_list:

        path = os.path.join(orgin_path, case,'SegmentationClassPNG')
        # path = os.path.join(path_before, 'SegmentationClassPNG')
        print(case)


        p = transforms.Compose([transforms.Resize((512, 512))])


        img_list = next(os.walk(path))[2]
        img_list.sort()

        numImage = len(img_list)

        xSize = 512
        ySize = 512
        vol_numpy = np.zeros((xSize, ySize, numImage))

        for t_i in img_list:
            # print(t_i)
            imagePIL = Image.open(path+'/'+ t_i)
            imagePIL = p(imagePIL)
            imageNP = np.array(imagePIL)

            for i in range(xSize):
                for j in range(ySize):
                    if imageNP[i][j] != 0:
                        imageNP[i][j] = 2

            # 0,1이 들어가는지 확인하
            #print(imageNP.max())

            # imshow(imageNP)
            # vol_numpy[:, :, img_list.index(t_i)] = imageNP  # To have labels in the range [0,1,2]
            vol_numpy[:, :, img_list.index(t_i)] = imageNP # To have labels in the range [0,1,2]



        # print(vol_numpy.shape)
        vol_numpy = vol_numpy.transpose((2,0,1))
        print(vol_numpy.shape)
        print(vol_numpy.max())
        #print(vol_numpy)

        xform = np.eye(4) * 2
        imgNifti = nib.nifti1.Nifti1Image(vol_numpy, xform)

        # output_path = '/Kidney_3D'
        # vol_nii_filename = output_path + / + s_i + '.nii.gz'
        # imgNifti.to_filename(str(vol_nii_filename))

        # niftiName = output_path / f'prediction_{s_i:03d}.nii.gz'


        niftiName = 'blad_seg_{0:05d}.nii.gz'.format(int(case_list.index(case)))

        output_path = '/home/has/Datasets/Bladder_240.nii/'
        if os.path.isdir(output_path)==False:
            os.makedirs(output_path)

        nib.save(imgNifti, output_path+niftiName)

img_2_nifti()







# nifti 이미지 읽기
# import nibabel
# img = nibabel.load('Results/Images/Nifti/Subj_181.nii')
# img_data = img.get_fdata()
# print(img.shape)  #(256,256,15)성




# 폴더 연속 생
# path = 'val_gt/'
# val_list = next(os.walk(path))[1]
# print(val_list)
# for i in range(230, 239):
#     os.makedirs(path + 'Subj_'+ str(i))




