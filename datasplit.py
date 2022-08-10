# import numpy as np
# import os
import pandas as pd


# normal_path = "data/all_images/Normal"
# n_dir_list = os.listdir(normal_path)

# n_df = pd.DataFrame(n_dir_list, columns = ['image_id'])
# n_df['dr'] = 0

# n_train, n_validate, n_test = np.split(n_df.sample(frac=1, random_state=42), 
#                        [int(.70*len(n_df)), int(.85*len(n_df))])

# pneumonia_path = "data/all_images/Pneumonia"
# p_dir_list = os.listdir(pneumonia_path)

# p_df = pd.DataFrame(p_dir_list, columns = ['image_id'])
# p_df['dr'] = 1
# p_df

# p_train, p_validate, p_test = np.split(p_df.sample(frac=1, random_state=42), 
#                        [int(.70*len(p_df)), int(.85*len(p_df))])

# tuberculosis_path = "data/all_images/Tuberculosis"
# t_dir_list = os.listdir(tuberculosis_path)

# t_df = pd.DataFrame(t_dir_list, columns = ['image_id'])
# t_df['dr'] = 2
# t_df

# t_train, t_validate, t_test = np.split(t_df.sample(frac=1, random_state=42), 
#                        [int(.70*len(t_df)), int(.85*len(t_df))])

# train_xrays = pd.concat([n_train, p_train, t_train])
# val_xrays = pd.concat([n_validate, p_validate, t_validate])
# test_xrays = pd.concat([n_test, p_test, t_test])

# train_xrays.to_csv('data/train_xrays.csv', index = False)
# val_xrays.to_csv('data/val_xrays.csv', index = False)
# test_xrays.to_csv('data/test_xrays.csv', index = False)

# all_images = pd.concat([p_df,n_df,t_df])
# all_images.to_csv('data/all_images.csv', index = False)


# import matplotlib.pyplot as plt

# all_images = pd.read_csv("data/all_images.csv")
# plt.figure()
# all_images['dr'].value_counts().plot(kind = 'bar')



train_xrays = pd.read_csv('data/train_xrays.csv')
val_xrays = pd.read_csv('data/val_xrays.csv')
test_xrays = pd.read_csv('data/test_xrays.csv')

shuffled_train = train_xrays.sample(frac=1, random_state=1).reset_index()
shuffled_val = val_xrays.sample(frac=1, random_state=1).reset_index()
shuffled_test = test_xrays.sample(frac=1, random_state=1).reset_index()

shuffled_train.to_csv('data/train_xrays1.csv', index = False)
shuffled_val.to_csv('data/val_xrays1.csv', index = False)
shuffled_test.to_csv('data/test_xrays1.csv', index = False)


