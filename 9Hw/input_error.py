def input_error(func):
    def debug(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Phone's number is not correct!"
        except IndexError:
            return "Give me name and phone please"
        except KeyboardInterrupt:
            return "Good bye"

    return debug