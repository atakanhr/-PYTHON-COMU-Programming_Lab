class myClass():
    def __init__(self, myfile = " "):
        f = open("deneme.txt", "r")
        myContent = f.read()
        Sentences = myContent.split(".")
        self.Words=[]
        for sentence in Sentences:
            Words_in_the_sentence = sentence.split(" ")
            for word_1 in Words_in_the_sentence:
                self.Words.append(word_1)
        self.my_frequency_1()
        self.my_frequency_2()
        self.write_frequency_1()
        self.write_frequency_2()
        

    def my_frequency_1(self):
        self.frequency_list_1 = {}
        for word in self.Words:
            if(word in self.frequency_list_1):
                self.frequency_list_1[word] += 1 
            else:
                self.frequency_list_1[word] = 1

    def write_frequency_1(self):
        for word_1 in self.frequency_list_1:
            print(word_1+ " " + str(self.frequency_list_1[word_1]))


    def my_frequency_2(self):
        self.frequency_list_2 = {}
        for i in range(len(self.Words)-1):
            w_1,w_2 = self.Words[i],self.Words[i+1]
            if ((w_1,w_2) in self.frequency_list_2):
                self.frequency_list_2[(w_1,w_2)] += 1 
            else:
                self.frequency_list_2[(w_1,w_2)] = 1


    def write_frequency_2(self):
        for w_1 in self.frequency_list_2:
            print(str(w_1)+ " " + str(self.frequency_list_2[w_1]))

my_class_1 = myClass()
print(len(my_class_1.Words))
my_class_1.my_frequency_1()
print(my_class_1.Words,end=" ")
