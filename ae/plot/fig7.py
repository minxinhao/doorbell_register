import matplotlib.pyplot as plt 
from matplotlib.pyplot import MultipleLocator
import numpy as np
import csv
from matplotlib.ticker import StrMethodFormatter, NullFormatter
from matplotlib import gridspec
import common

# Configuration
threads = common.thread_set


# DO NOT CHANGE BELOW
def load_dataset(dataset_path):
    with open(dataset_path) as dataset:
        data_reader = csv.reader(dataset, delimiter=",")
        table = []
        for data in data_reader:
            table.append(float(data[7]))
        return np.reshape(table, [len(table) // len(threads), len(threads)])


def load_dataset_scaleout(dataset_path):
    with open(dataset_path) as dataset:
        data_reader = csv.reader(dataset, delimiter=",")
        table = []
        for data in data_reader:
            table.append(float(data[7]))
        return np.reshape(table, [2, len(table) // 2])
    

def set_single_plt():
    fig = plt.figure(figsize=(16.0, 2.35))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Arial']
    plt.rcParams['mathtext.fontset'] = 'cm'
    plt.rcParams['font.size'] = 18
    plt.rcParams['hatch.linewidth'] = 0.90
    return fig

def plot_figure(ax, data):
    ax.plot(threads, data[3], marker='v', color="darkblue", label="SMART-HT", linewidth=1, ms=8, markerfacecolor='white')
    ax.plot(threads, data[0], marker='D', color="purple", label="RACE", linewidth=1, ms=8, markerfacecolor='white')
    ax.set_xlim([0, 100])
    ax.grid(linestyle='-.')


def plot_figure2(ax, data):
    X = (1 + np.array(range(6))) * 96 / 100.0
    ax.plot(X, data[0], marker='D', color="purple", label="RACE", linewidth=1, ms=8, markerfacecolor='white')
    ax.plot(X, data[1], marker='v', color="darkblue", label="SMART-HT", linewidth=1, ms=8, markerfacecolor='white')
    ax.set_xlim([0, 6])
    ax.set_xticks([0, 2, 4, 6])
    ax.grid(linestyle='-.')

def draw_graph(path):
    fig = set_single_plt()
    gs = gridspec.GridSpec(1, 6, width_ratios=[2,2,2,1.2,1.2,1.2]) 
    ax = fig.add_subplot(gs[0])
    ax.set_title("(a) Write-heavy", size=18)
    data = load_dataset(common.ae_data_path + "/fig8-ycsb-a.csv")
    plot_figure(ax, data)
    ax.set_ylabel("Throughput (MOP/s)", size=16.2)
    ax.set_ylim([0, 8])
    ax.set_yticks([0, 4, 8])

    h1, l1 = ax.get_legend_handles_labels()
    plt.legend(h1, l1, loc="best", bbox_to_anchor=(0.2, 0.2, 0.5, 0.5), borderaxespad=0, frameon=False, ncol=1, handletextpad=0.3)

    ax = fig.add_subplot(gs[1])
    ax.set_title("(b) Read-heavy", size=18)
    data = load_dataset(common.ae_data_path + "/fig8-ycsb-b.csv")
    plot_figure(ax, data)
    ax.set_xlabel("Thread Count")
    ax.set_ylim([0, 30])
    ax.set_yticks([0, 10, 20, 30])

    ax = fig.add_subplot(gs[2])
    ax.set_title("(c) Read-only", size=18)
    data = load_dataset(common.ae_data_path + "/fig8-ycsb-c.csv")
    plot_figure(ax, data)
    ax.set_ylim([0, 30])
    ax.set_yticks([0, 10, 20, 30])

    ax = fig.add_subplot(gs[3])
    ax.set_title("(d) Write-heavy", size=18)
    data = load_dataset_scaleout(common.ae_data_path + "/fig7-ycsb-a.csv")
    plot_figure2(ax, data)
    ax.set_ylim([0, 8])
    ax.set_yticks([0, 2, 4, 6, 8])

    ax = fig.add_subplot(gs[4])
    ax.set_title("(e) Read-heavy", size=18)
    data = load_dataset_scaleout(common.ae_data_path + "/fig7-ycsb-b.csv")
    plot_figure2(ax, data)
    ax.set_xlabel("Thread Count ($\\times 100$)")
    ax.set_ylim([0, 60])
    ax.set_yticks([0, 20, 40, 60])

    ax = fig.add_subplot(gs[5])
    ax.set_title("(f) Read-only", size=18)
    data = load_dataset_scaleout(common.ae_data_path + "/fig7-ycsb-c.csv")
    plot_figure2(ax, data)
    ax.set_yticks([0, 40, 80, 120])
    ax.set_ylim([0, 120])

    plt.tight_layout(pad=0)
    plt.savefig(path, bbox_inches='tight', pad_inches=0)
    plt.close()

draw_graph(common.ae_figure_path + "/fig7.pdf")
