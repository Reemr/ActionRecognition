
import os
import glob

def createClassIndList(movie_dir, list_dir,class_dest):

    movie_cat_list = os.listdir(movie_dir)
    classind = {}

    for c,fi in enumerate(movie_cat_list):
        classind[fi] = c

    with open(class_dest, 'w') as f:
        for k,v in classind.items():
            f.write('{}'.format(v) + ' ' +k+'\n')
    return classind

def createTraintestLists(movie_dir, train_dest, test_dest, classind):

    with open(train_dest, 'w') as tr, open(test_dest, 'w') as ts:
        for fol in classind.keys():
            data_path = os.path.join(movie_dir,fol)
            data_list = os.listdir(data_path)
            #print(data_list)
            for i,fil in enumerate(data_list):
                fil_pa = os.path.join(fol,fil)
                #print(fil_pa)
                if i < 3:
                    tr.write(fil_pa + '\n')
                else:
                    ts.write(fil_pa + '\n')

if __name__ == '__main__':

    data_dir = 'C:\\Users\\Reem\\Projects\\ActionRecognition\\data'
    movie_dir = os.path.join(data_dir, 'Movie_dataset_sample')
    list_dir = os.path.join(data_dir, 'movieTrainTestlist')

    class_dest = os.path.join(list_dir,'classInd.txt')
    class_ind = createClassIndList(movie_dir, list_dir, class_dest)

    train_dest = os.path.join(list_dir, 'trainlist0.txt')
    test_dest = os.path.join(list_dir, 'testlist0.txt')
    createTraintestLists(movie_dir, train_dest, test_dest, class_ind)
