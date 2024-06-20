import torch

# .pt 파일 경로
pt_file_path = "/home/eunseo/AUE8088-PA2/yolov5n.pt"

# 체크포인트 로드
checkpoint = torch.load(pt_file_path, map_location="cpu")

# 전체 체크포인트 출력
# print("Checkpoint contents:")
# print(checkpoint)

# 모델 가중치만 출력 (만약 저장된 것이 state_dict일 경우)
# if 'model' in checkpoint:
#     state_dict = checkpoint['model']
#     print("Model state_dict:")
#     for k, v in state_dict.items():
#         print(k, v.shape)
# else:
#     print("State dict:")
#     for k, v in checkpoint.items():
#         print(k, v.shape)

if 'anchor' in checkpoint:
    state_dict = checkpoint['anchor']
    for k, v in state_dict.items():
        print(k, v.shape)
else:
    print("State dict:")
    # for k, v in checkpoint.items():
    #     print(k, v.shape)