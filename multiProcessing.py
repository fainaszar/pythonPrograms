import os

from multiprocessing import Process, current_process


def doubler(number):

	result = number * 2
	process_name = current_process.name()
	print("{} doubled to {} by {}")