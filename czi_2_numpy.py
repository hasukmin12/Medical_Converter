import slideio
import cv2
slide = slideio.open_slide("/home/has/PycharmProjects/my_code/czi_reader/lupus/S20_7036(Silver).czi", "CZI")
scene = slide.get_scene(0)
# image = scene.read_block()  # 이렇게하면 원본 영상을 출력
image = scene.read_block(size=(500,0))





print(image.shape)
cv2.imshow('czi',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


num_scenes = slide.num_scenes
for index in range(0, num_scenes):
   print(slide.get_scene(index).name)

