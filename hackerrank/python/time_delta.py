"""
https://www.hackerrank.com/challenges/python-time-delta/problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains lines, representing time and time .

Constraints

    Input contains only valid timestamps
    .

Output Format

Print the absolute difference in seconds.

Sample Input 0

    2
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000

Sample Output 0

    25200
    88200

Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is seconds or seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or
"""
from datetime import datetime, timedelta


def get_date(date_string):
    """

    :param date_string: Sun 10 May 2015 13:54:36 -0700
    :return:
    """
    return datetime.strptime(date_string[:-6], '%a %d %b %Y %H:%M:%S'), date_string[-5], timedelta(hours=int(date_string[-4:-2]), minutes=int(date_string[-2:]))


def get_utc_date(date_string):
    """

    :param date_string: Sun 10 May 2015 13:54:36 -0700
    :return:
    """
    timestamp, tmz, tmz_diff = get_date(date_string)
    timestamp = timestamp + tmz_diff if tmz is '-' else timestamp - tmz_diff
    return timestamp


if __name__ == "__main__":
    inputs = int(input().strip())

    for _ in range(inputs):
        date1, date2 = get_utc_date(input().strip()), get_utc_date(input().strip())
        diff = abs(date1 - date2)
        print(diff.days * 86400 + diff.seconds)


"""
Test Case:

    2
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
"""