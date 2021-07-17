# # heuristc - correct path to go down 
# # f = g + n 
# # h(n) -> estimate from current node to end 
# # g(n) -> fron current node to some node 
# # Store each path and weight from each point 
# # Last indicates our parent node or where 
# # we came from

# NODE G H F 
# 0,1  0 6 6
# 0,2  1 5 6
# 0,0  1 7 8 
# 0,3  2 4 6 
# 0,4  3 5 8
# 1,0  2 6 8 
# 2,0  3 5 8
# 1,4  4 4 8
# 2,1  4 4 8 
# 2,4  5 3 8 
# 2,1  4 4 8
# 2,2  5 3 8


# sample input 
#[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]

# how to make it greedy? 
# the starting point should be assigned! 
# after that we can compare the len(steps) on other nodes apart from 
# the end node. 
# a -> b = 10 
# a -> c = 12
# b-> c =8
# b -> d = 9 
# c -> b 10 
# c -> D 5 
# a -> b -> c -> d = 10 + 8 + 5 = 23 
# a -> c -> b -> d = 12 + 10 + 9 = 31    
    
    
    
    # We are sure this problem could be solved more optimally with the approach down below but due to time constraints
    # we could not finish it. 
    # The approach is greedy because we are taking the best possible choice at each 
    # point. This problem is a variation of the traveling salesman optimization problem, which is an np-complete 
    # problem. 
    # https://en.wikipedia.org/wiki/Travelling_salesman_problem
    # We considered approaches like minimum spanning tree and finally landed on A*(manhattan algorithm) because we wanted to take 
    # the greedy approach after computing the distance from each point. 
    # Much like memoization(which can be defined as an optimization technique to speed up programs by storing the results of expensive 
    # function calls and returning cached results when same input occurs again), to utilize this 
    # in Target stores, we can store path combinations in a database and make API calls to find each subpath and computing 
    # full path based on the store and department. 
        # for k,v in self.check_points.items():
        #     k_l = k.split(' ')
        #     if k_l[0] not in self.min_check_point and k_l[0] not in self.in_route and k_l[1]!='check_out':
        #         print('1')
        #         if k_l[1] not in self.in_route:
        #             self.min_check_point[k_l[0]]=(k_l[1],len(v)) 
        #             self.in_route[k_l[1]]=1
        #     elif k_l[0] in self.min_check_point and k_l[1] in self.in_route:
        #         print(2)
        #         continue 
        #     else:
        #         print(3)
        #         y= k_l[0]
        #         if k_l[0] not in self.min_check_point and k_l[0] in self.in_route:
        #             if k_l[1] not in self.min_check_point and k_l[1] not in self.in_route:
        #                 self.min_check_point[k_l[0]]=(k_l[1],len(v)) 
        #                 self.in_route[k_l[1]]=1 

                    
        #         elif y in self.min_check_point:
        #             weight=self.min_check_point[k_l[0]] 
        #             if weight[1]> len(v) and k_l[1] and k[1] not in self.in_route and k_l[1]!='check_out' :
        #                 self.min_check_point[k_l[0]]=(k_l[1],len(v)) 
        #                 del  self.in_route[weight[0]]
        #                 self.in_route[k_l[1]]=1
            # print('start: ', k_l[0],'destination: ', k_l[1])
            # print('min_check_point:',self.min_check_point)
            
        #     print('route:',self.in_route)
        # print(self.min_check_point)
        # for k,v in self.check_points.items():
        #     k_ll = k.split(' ')
        #     self.in_route[k_ll[0]]=1 
        #     for key,value in self.check_points.items():
        #         k_l = key.split(' ')
        #         if k_l[1] in self.in_route:
        #             continue 
        #         elif k_ll[0] == k_l[0]:
        #             if k_l[0] not in self.min_check_point and k_l[1]!='check_out' and k_l[0]==k_ll[0]:
        #                 self.min_check_point[k_l[0]]=(k_l[1],len(value))
        #             else: 
        #                 if k_l[1]!='check_out' and k_ll[0] in self.min_check_point: 
        #                     weight = self.min_check_point[k_l[0]]
        #                     if weight[1]>=len(value):
        #                         self.min_check_point[k_ll[0]]=(k_l[1],len(value))
        #         else:
        #             continue
        # Now that we have all possible path from each point to the next we can focus on 
        # generating a full path which visits all the points.
Listfromfrontend= [
    {
     'name':'oil',
     'category':'automotive'
    },
    {
    'name':'easter egg',
    'category':'seasonal'}
    , {'name':'turkey',
    'category':'deli'}
    , {
        'name':'showerhead',
        'category':'bath'
    },
    {
        'name':'showerhead',
        'category':'personal_care'
    },
            {
     'name':'barbie',
     'category':'toys'
    }
    ]
section_map={'entertainment': (2, 19), 'tech': (2, 31), 'automotive': (3, 3), 'home_improvement': (3, 11), 'sporting_good': (3, 44), 
'seasonal': (3, 53), 'school': (4, 50), 'storage': (8, 3), 'hoisery': (8, 17), 'baby': (10, 26), 'infant': (13, 37), 'kid': (15, 28),
 'bedding': (16, 3), 'toys': (16, 43), 'intimates': (17, 16), 'girls': (17, 30), 'kitchen': (20, 22), 'snacks': (20, 52), 'boys': (21, 30), 
 'wine': (22, 54), 'bath': (25, 3), 'maternity': (27, 22), 'travel': (28, 43), 'active_wear': (29, 16), 'gr': (29, 51), 'shoes': (31, 32), 
 'furniture': (34, 3), 'accessories': (34, 15), 'fitting_rooms': (34, 26), 'mens': (34, 37), 'car': (36, 9), 'household': (36, 43), 
 'womens': (38, 22), 'guest_service': (39, 15), 'deli': (40, 51), 'bakery': (42, 50), 'seafood': (42, 52), 'health_beauty': (46, 37), 'Rest_room': (47, 3), 
'check_out': (47, 16), 'personal_care': (47, 43), 'beauty': (48, 29), 'household_paper': (48, 51), 'starbucks': (52, 12), 'pharmacy': (53, 37), 
'pets': (53, 51), 'entrance': (55, 6)}
