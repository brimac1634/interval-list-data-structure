from __future__ import annotations
from functools import reduce
from typing import List


Interval = List[int]

class IntervalList:
    """
    IntervalList: Data structure that stores intervals of integers
    """
    
    def __init__(self) -> None:
        self._intervals = []


    def __lt__(self, other_interval_list: IntervalList) -> bool:
        return self.__total() < other_interval_list.__total()

    
    def __gt__(self, other_interval_list: IntervalList) -> bool:
        return self.__total() > other_interval_list.__total()

    
    def __le__(self, other_interval_list: IntervalList) -> bool:
        return self.__total() <= other_interval_list.__total()

    
    def __ge__(self, other_interval_list: IntervalList) -> bool:
        return self.__total() >= other_interval_list.__total()

    
    def __eq__(self, other_interval_list: IntervalList) -> bool:
        return self.__total() == other_interval_list.__total()

    
    def __contains__(self, other_interval_list: IntervalList) -> bool:
        if other_interval_list.__total() < 1:
            return True
        elif self.__total() < 1 or self.__total() < self.__total():
            return False
        else:
            i = j = 0
            while i < len(other_interval_list._intervals) and j < len(self._intervals):
                if other_interval_list._intervals[i][0] >= self._intervals[j][0] and other_interval_list._intervals[i][1] <= self._intervals[j][1]:
                    i += 1
                else:
                    j += 1

            return False if i < len(other_interval_list._intervals) else True
            


    def __assert_interval(self, interval: Interval) -> None:
        """
        Asserts correct interval data structure
            Parameters:
                interval (Interval): interval to be checked for correct structure
        """
        assert isinstance(interval, List), f"interval must be a list, got: {type(interval)}"
        assert all(isinstance(item, int) for item in interval), f"interval must be a list containing 2 integers, got: {interval}"
        assert interval[0] <= interval[1], f"the first integer in the interval must be less than or equal to the second integer, got: {interval}"


    def __total(self) -> int:
        """
        Gets aggregated total of all interval ranges
            Returns:
                total (int)
        """
        return reduce(lambda x, y: x + y[1] - y[0], self._intervals, 0)

    @property
    def intervals(self) -> List[Interval]:
        """
        Get list accessor for testing purposes
            Returns:
                interval list (List[List[int]])
        """
        return self._intervals


    def add(self, new_interval: Interval) -> None:
        """
        Adds new interval to interval list if not already included in current list
            Parameters:
                interval (Interval): interval to be added to the interval list
        """
        self.__assert_interval(new_interval)

        current_intervals = self._intervals
        current_intervals_length = len(current_intervals)

        if current_intervals_length < 1:
            current_intervals.append(new_interval)
            return      

        updated_list = []
        i = 0

        """
            insert existing intervals that come before the new interval and 
            get to the index of where the new interval starts 
        """
        while i < current_intervals_length and current_intervals[i][1] < new_interval[0]:
            updated_list.append(current_intervals[i])
            i += 1
        
        """
            iterate through intervals that fall within the new interval and 
            calculate the minimum start and maximum end of the new interval to be inserted
        """
        start = new_interval[0]
        end = new_interval[1]
        while i < current_intervals_length and current_intervals[i][0] <= new_interval[1]:
            start = min(start, current_intervals[i][0])
            end = max(end, current_intervals[i][1])
            i += 1
        
        updated_list.append([start, end])

        while i < current_intervals_length:
            updated_list.append(current_intervals[i])
            i += 1

        self._intervals = updated_list 





    def remove(self, interval_to_remove: Interval) -> None:
        """
        Removes interval from interval list if included in current list
            Parameters:
                interval (Interval): interval to be removed from the interval list
        """
        self.__assert_interval(interval_to_remove)

        current_intervals = self._intervals
        current_intervals_length = len(current_intervals)

        if current_intervals_length < 1:
            return   

        updated_list = []
        i = 0

        # insert existing intervals that come before the interval to remove
        while i < current_intervals_length and current_intervals[i][1] < interval_to_remove[0]:
            updated_list.append(current_intervals[i])
            i += 1

        # re-insert adjusted intervals at the beginning and end of the interval to remove 
        while i < current_intervals_length and current_intervals[i][0] <= interval_to_remove[1]:
            if current_intervals[i][0] < interval_to_remove[0] and current_intervals[i][1] > interval_to_remove[1]:
                updated_list.append([current_intervals[i][0], interval_to_remove[0]])
                updated_list.append([interval_to_remove[1], current_intervals[i][1]])
            elif current_intervals[i][0] < interval_to_remove[0] and current_intervals[i][1] <= interval_to_remove[1]:
                updated_list.append([current_intervals[i][0], interval_to_remove[0]])
            elif current_intervals[i][1] > interval_to_remove[1] and current_intervals[i][0] <= interval_to_remove[1]:
                updated_list.append([interval_to_remove[1], current_intervals[i][1]])
            i += 1  

        while i < current_intervals_length:
            updated_list.append(current_intervals[i])
            i += 1

        self._intervals = updated_list 
        



    def print(self) -> None:
        """
        Prints out the list of intervals in the interval list  
        """
        print(' '.join(map(str, self._intervals)))

