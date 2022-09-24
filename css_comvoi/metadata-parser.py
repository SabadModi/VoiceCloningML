counterIndex = 30000
times = 0
with open("css_comvoi/n_train.txt", "r", encoding="utf-8") as f:
    with open("css_comvoi/train.txt", "w", encoding="utf-8") as f2:
        for line in f:
            # print(line)
            # break
            times+=1
            lineArr = line.split("|")
            # print(lineArr)
            # break
            lineArr.pop(0)
            # lineArr.pop(2)
            lineArr.insert(0, "0"+str(counterIndex))
            counterIndex -= 1
            lineArr.insert(1,"fr")
            lineArr.insert(1,"fr")
            lineArr.insert(4, "linear_spectrograms\\0"+str(counterIndex)+".npy")
            lineArr.insert(4, "spectrograms\\0"+str(counterIndex)+".npy")
            lineArr.insert(7, "")
            lineArr[6] = lineArr[6].replace("\n", "").replace("\t", "")
            lineArr[3] = "wavs/"+lineArr[3]
            # print(lineArr)
            # break
            # print("|".join(lineArr))
            f2.write("|".join(lineArr)+"\n")