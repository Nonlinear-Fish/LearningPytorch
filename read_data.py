from torch.utils.data import Dataset
from PIL import Image
import os#python的一个系统相关的库
class myDataSet(Dataset):

    def __init__(self, root_dir, label_dir):
        #暂时理解为this
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(root_dir, label_dir)
        self.img_path = os.listdir(self.path)


    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.path, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = "hymenoptera_data/train"
label_dir = "bees"
ants_dataSet = myDataSet(root_dir, label_dir)
