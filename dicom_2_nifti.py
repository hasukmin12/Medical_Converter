import dicom2nifti
import os


dicom_directory = '/home/has/Datasets/_has_CT3'
# dicom_directory = '/home/has/Datasets/CV_CT/slice_5'
dicom_folder = next(os.walk(dicom_directory))[1]
dicom_folder.sort()
print(dicom_folder)



for dicom_list in dicom_folder:
    print(dicom_list)
    output_path = '/home/has/Datasets/(has)CT_nii/case_' + '{0:05d}'.format(dicom_folder.index(dicom_list))
    os.makedirs(output_path)
    input_path = dicom_directory + '/' + dicom_list
    print(input_path)
    dicom2nifti.convert_directory(input_path, output_path, compression=True, reorient=True)
    # dicom2nifti.convert_directory(dicom_directory, output_path, compression=True, reorient=True)
    # icom2nifti.dicom_series_to_nifti(dicom_directory +'/'+dicom_list, output_path, reorient_nifti=True)