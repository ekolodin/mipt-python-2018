import matplotlib.pyplot as plt


def show_hist(sample):
    plt.figure(figsize=(10, 4))
    plt.hist(sample, bins=8, alpha=0.4, color='orange')
    plt.xlabel('average')
    plt.ylabel('students')
    plt.grid(ls=':')
    plt.show()


with open('averages.txt', 'r') as f:
    show_hist([int(i) for i in f.read().split()])
