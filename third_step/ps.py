import os
import matplotlib.pyplot as plt


def show(page):
    page = page.split(".")[0]
    plt.savefig(os.path.join(f'third_step/img/{page}.png'), dpi=80, format='png', bbox_inches='tight')