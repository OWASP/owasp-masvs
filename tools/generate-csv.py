#!/usr/bin/python

""" Quick and Dirty Roberto Martelloni's script to generate a CSV """

import os


def fromFilenameToArea(filename):
    splittedFilename = filename.split("-")
    id = splittedFilename[1]
    name = splittedFilename[2].split(".")
    name = name[0].replace("_", " ")

    return id, name



def parsemd(filename):

    for line in open(filename):
        if line.startswith("|"):
            if line.find("| --- |") == 0: continue
            if line.find("| # |") == 0: continue
            if line.find("|  #") == 0: continue

            start = fromFilenameToArea(filename)
            line = line.replace("*", "")
            line = line.split("|")
            print(start[0] + "|", end=' ')
            print(start[1] + "|", end=' ')
            print(line[1] + "|", end=' ')
            print(line[2] + "|", end=' ')
            print(line[3] + "|", end=' ')
            print(line[4] + "|")


def main():
    for file in os.listdir("./Document"):
        if file.find("-V") != -1:
            parsemd("./Document/" + file)


if __name__ == '__main__':
    main()
