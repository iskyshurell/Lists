# import functools
#
# def singleton(cls):
# 	@functools.wraps(cls)
# 	def wrapped(*args, **kwargs):
# 		if not wrapped.status:
# 			status = cls(*args, **kwargs)
#
# 		return wrapped.status
#
# 	wrapped.status = None
# 	return wrapped
#
# @singleton
# class Example:
# 	pass
#
#
# my_obj = Example()
# my_another_obj = Example()
# to = Example()
#
# print(id(my_obj))
# print(id(my_another_obj))
#
# print(my_obj is to)
# print(my_obj is my_another_obj)