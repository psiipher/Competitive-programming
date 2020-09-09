'''
https://leetcode.com/problems/count-number-of-teams/
'''

def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i, v in enumerate(rating):
            llc = lgc = rlc = rgc = 0
            for l in rating[:i]:
                if l < v:
                    llc += 1
                elif l > v:
                    lgc += 1
            for r in rating[i+1:]:
                if r < v:
                    rlc += 1
                elif r > v:
                    rgc += 1
            count += (llc * rgc) + (lgc * rlc)
        return count
        
        
'''

So here is how it works.

We are going to have a main for loop and we are going to pick one element from the ratings list at a time. Then we are going to have two other loops. One is going to scan all elements before and the other one is going to scan all elements after. Those two loops will count number of elements less and greater than the one we picked. So let's say we have 2 elements less than the selected one to the left and 3 elements greater to the right. That means the number of ascending sequences we can build is 2 * 3 = 6 . Now we just need to extend the same logic to all descending sequences and return the total.

First, let's define the variables. Technically we can use just one counter, but for clarity, let's use two, asc for ascending and dsc for descendig sequences:

        asc = dsc = 0

Now let's start our main loop to scan all elements:

        for i,v in enumerate(rating):

Inside every cycle we are going to use 4 local counters: llc - stands for Left, Less, Counter - count of elements less then the current one to the left. rgc - Right, Greater, Counter - count of elements greater than the current one to the right. I think you can guess what the other 2 are?

            llc = rgc = lgc = rlc =0

Ok, now we picked some element, we are going to look to the left and count element less and greater than the current one:

            for l in rating[:i]:
                if l < v:
                    llc += 1
                if l > v:
                    lgc += 1

And now we look to the right:

            for r in rating[i+1:]:
                if r > v:
                    rgc += 1
                if r < v:
                    rlc += 1

And update the total counters:

            asc += llc * rgc
            dsc += lgc * rlc            

Once the main loop is complete, we just return the total total:

        return asc + dsc

Ok, all done!

We can add some polishing touches:

    1. Since we really need just one counter, we can replace asc and dsc with a single counter c.
    2. Since we need to have same elements to the left and to the right, we can skip the the first and the last elements in the main loop scan.
    3. Replace 2nd if with elsif - that would reduce number of logical operations - since if the first condition is True, the second won't be evaluated.

Explained by : https://leetcode.com/rmoskalenko
'''
