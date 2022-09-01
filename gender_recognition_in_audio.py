importimport amfm_decompy.pYAAPT as pYAAPT
import amfm_decompy.basic_tools as basic
pitchY = [0]
s = 0
print('введите количество аудиозаписей')
n = int(input())
for i in range(1, n+1):
    signal = basic.SignalObj('{id}.wav'.format(id=i))
    filename = '{id}.wav'.format(id=i)
    print(filename, end=' ')
    pitchY.append(pYAAPT.yaapt(signal, frame_length=35, tda_frame_length=35, f0_max=600))
    minS = 2000
    maxS = 0
    sumS = 0
    j = 0
    for t in range(len(pitchY[i].samp_values)):
        if float(pitchY[i].samp_values[t]) > 0:
            sumS += float(pitchY[i].samp_values[t])
            j += 1
            if minS > float(pitchY[i].samp_values[t]):
                minS = float(pitchY[i].samp_values[t])
            if maxS < float(pitchY[i].samp_values[t]):
                 maxS = float(pitchY[i].samp_values[t])
    if sumS/j > 155:
        print('женщина')
    else:
        print('мужчина')


