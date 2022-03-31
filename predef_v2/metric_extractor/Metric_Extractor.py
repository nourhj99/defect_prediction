from radon.complexity import average_complexity, cc_visit
from radon.raw import analyze
from radon.metrics import h_visit
import torch
class Metric_Extractor(object):
    """docstring for Metric_Extractor"""
    def __init__(self,filename):
        super(Metric_Extractor, self).__init__()
        with open(filename) as fobj:
            self.sourceFile = fobj.read()
        self.rawMetrics = self.generateRawMetrics()
        self.mcCabeMetrics = self.cyclomaticComplexity()
        self.halsteadMetrics = self.generateHalsteadMetrics()
    #Cyclomatic Complexity
    def cyclomaticComplexity(self):
        cc = cc_visit(self.sourceFile)
        return average_complexity(cc)

    def generateRawMetrics(self):
        raw = analyze(self.sourceFile)
        return raw

    def generateHalsteadMetrics(self):
        hl = h_visit(self.sourceFile)
        return hl
        
    def numberOfOperators(self):
        return self.halsteadMetrics.total[0]

    def numberOfOperands(self):
        return self.halsteadMetrics.total[1]

    def totalNumberOfOperators(self):
        return self.halsteadMetrics.total[2]

    def totalNumberOfOperands(self):
        return self.halsteadMetrics.total[3]

    def halsteadProgramLength(self):
        return self.halsteadMetrics.total[5]

    def linesOfCode(self):
        return self.rawMetrics.lloc

    def volume(self):
        return self.halsteadMetrics.total[7]

    def effort(self):
        return self.halsteadMetrics.total[9]

    def linesOfComments(self):
        return self.rawMetrics.comments










