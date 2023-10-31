class Solution:
    def findRestaurant(self, list1, list2):
        
        list_com = []
        list_com_indexsum = []

        if len(list1) <= len(list2):
            for i in list1:
                if i in list2:
                    list_com.append(i)
        else:
            for i in list2:
                if i in list1:
                    list_com.append(i) 
        
        for i in list_com:
            list_com_indexsum.append(list1.index(i) + list2.index(i))
        
        result_dict = {}

        for count, word in zip(list_com_indexsum, list_com):
            if count in result_dict:
                result_dict[count].append(word)
            else:
                result_dict[count] = [word]
        
        print(result_dict[min(list_com_indexsum)])

        


list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

Solution().findRestaurant(list1, list2)