import random

# 重複なし
def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

class IntroDon():

    now_point = 0
    now_problem = 0
    music_list = [
        "マリーゴールド",
        "進撃の巨人",
        "くら寿司",
        "ハムす",
        "れいこ",
    ]
    # used_numList = []
    answer_number = None
    choices_list = None

    def reset(self):
        self.answer_number = None
        self.choices_list = None
        self.now_point = 0
        self.now_problem = 0

    def GetPoint(self):
        return self.now_point

    def GetNowProblem(self):
        return self.now_problem
    
    def Move2NextProblem(self):
        self.now_problem += 1
        print("self.now_problem: ",self.now_problem)
        list_size = len(self.music_list)
        self.choices_list = rand_ints_nodup(0,list_size-1,3)
        # print("select_list: ",self.choices_list)
        self.answer_number = self.choices_list[random.randint(0,len(self.choices_list)-1)]
        sent_wav = self.music_list[self.answer_number] + ".mp3"
        choices_names_list = [self.music_list[index] for index in self.choices_list]
        return sent_wav, choices_names_list
    
    def AnswerTheQuestion(self, chosen_number):
        print("AnswerTheQuestion: Start!!")
        print("self.choices_list: ",self.choices_list)
        print("chosen_number: ",self.choices_list[chosen_number])
        print("self.answer_number: ",self.answer_number)
        if self.choices_list[chosen_number]==self.answer_number:
            self.now_point += 1
            return True
        else:
            return False

if __name__ == "__main__":
    test = IntroDon()
    while True:
        print(test.Move2NextProblem())
        inp_num = input()
        inp_num = int(inp_num)
        print(test.AnswerTheQuestion(inp_num))