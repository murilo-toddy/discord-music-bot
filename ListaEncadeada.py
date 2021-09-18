import collections
import random

class No:
    def __init__(self, url):
        self.url = url
        self.next = None

class ListaEncadeada:

    def __init__(self):
        self.head = None
        self.size = 0
        self.listaShuffle = []

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Indice fora de alcance")
        if pointer:
            return pointer
        else:
            raise IndexError("Indice fora de alcance")



     #Implements x = Lista[5] ; Pega o no e atribui a x

    def __setitem__(self,index,url):

        self.listaShuffle.append(url)

        pointer = self.head
        for i in range(index-1):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Indice fora de alcance")

        if index == 0:
            if pointer:
                NovoNo = No(url)
                NovoNo.next = self.head
                self.head = NovoNo
                self.size += 1
            else:
                NovoNo = No(url)
                self.head = NovoNo

        else :   
            if  pointer:
                NovoNo = No(url)
                NovoNo.next = pointer.next
                pointer.next = NovoNo
                self.size += 1
            else:
                raise IndexError("Indice fora de alcance")


    #Implements Lista[5]  = No_Generico ; Pega o no e atribui a x

    def append(self, url):

        self.listaShuffle.append(url)

        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = No(url)
            self.size += 1
        else:
            self.head = No(url)

    def remove(self,index):
        pointer = self.head
        for i in range(index-1):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Indice fora de alcance")
        if(index == 0):
            Noretorna = self.head

            self.head = self.head.next

            self.listaShuffle.remove(Noretorna.url)

            return Noretorna.url
        else: 
            if pointer and pointer.next:

                NoRemover = pointer.next
                pointer.next= NoRemover.next

                self.listaShuffle.remove(NoRemover.url)

                return NoRemover.url

            else:
                raise IndexError("Indice fora de alcance")

    def imprime(self):
        pointer = self.head
        if pointer:
            while(pointer.next != None):
                print(pointer.url)
                pointer = pointer.next
            print(pointer.url)

        else:
            print("Lista Vazia")

    def move(self, indiceInicial, IndiceFinal):
        url = self.remove(indiceInicial)
        self[IndiceFinal] = url


    def clean(self):
        self.head = None
        self.listaShuffle.clear()

    def shuffle(self):
        self.clean()
        random.shuffle(self.listaShuffle)   
        for i in range(len(self.listaShuffle)):
            self[0] = self.listaShuffle[i]


             