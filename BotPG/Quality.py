import numpy

class Quality():
    qualityDmgDict = {
        "Común": 0
        "Rara": 0.05
        "Épica": 0.1
        "Legendaria": 0.2
    }

    qualityProb = {
        "Común": 0.4
        "Rara": 0.4
        "Épica": 0.15
        "Legendaria": 0.05
    }

    qualityDict = {
        1: "Común"
        2: "Rara"
        3: "Épica"
        4: "Legendaria"
    }

    def __init__(self):
        self._name = qualityDict[numpy.random.choice(numpy.arange(1,len(qualityDict)+1), p=probabilities()])]
        self._qualityDmg = qualityDmgDict[name]

    def probabilities():
        a = []
        for q in qualityProb:
            a.append(qualityProb[q])
        return a

    def getQualityDmg():
        return self._bonus

