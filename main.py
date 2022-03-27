import matplotlib.pyplot as plt


if __name__ == "__main__":
    """
    Testing grounds...
    """
    plt.style.use("dark_background")
    plt.style.use("./styles/base.mplstyle")
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4])
    ax.set_ylabel("some numbers")
    ax.set_xlabel(xlabel="x-axis")
    ax.set_title("A simple plot")
    ax.legend(["some numbers"])
    plt.show()
