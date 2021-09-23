
import numpy as np
import nibabel as nib




vol_numpy2 = np.load('/home/has/Results/numpy_128.npy')
print(vol_numpy2.shape)

print(vol_numpy2)


xform = np.eye(4) * 2
label_Nifti = nib.nifti1.Nifti1Image(vol_numpy2, xform)

output_path = '/home/has/Results/128_CT_240.nii.gz'

nib.save(label_Nifti, output_path)
print("save nii")