import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from Neural_Net import dataset,Net
from torch.utils.data import Dataset, DataLoader
from torch import nn
#importing the dataset

df = pd.read_csv('./jm1.csv')
x = df[['uniq_Op','uniq_Opnd','total_Op','total_Opnd','l','loc','v(g)','lOComment','v','e']]
y = df[['defects']]
x = x.to_numpy()
y = y.to_numpy()
print("shape of x: {}\nshape of y: {}".format(x.shape,y.shape))
sc = StandardScaler()
x = sc.fit_transform(x)
print(x)
trainset = dataset(x,y)
trainloader = DataLoader(trainset,batch_size=64,shuffle=True)
learning_rate = 0.01
epochs = 10
# Model , Optimizer, Loss
model = Net(input_shape=x.shape[1])
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)
loss_fn = nn.BCELoss()

#forward loop
losses = []
accur = []
for i in range(epochs):
	for j,(x_train,y_train) in enumerate(trainloader):
		#calculate output
		output = model(x_train)

		#calculate loss
		loss = loss_fn(output,y_train.reshape(-1,1))

		#accuracy
		predicted = model(torch.tensor(x,dtype=torch.float32))
		acc = (predicted.reshape(-1).detach().numpy().round() == y).mean()
		#backprop
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
		print("epoch = ",i)
	if i%50 == 0:
		losses.append(loss)
		accur.append(acc)
		print("epoch {}\tloss : {}\t accuracy : {}".format(i,loss,acc))
torch.save(model,"./model.h")


plt.plot(losses)
plt.title('Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.show()
