import json
from model_dict import DictModel


class RequestInitializer:
    def __init__(self, **kwargs):
        """
        Initialization for request object

        :param kwargs: `config`: dict
        """
        self.config = kwargs["config"]
        self.req = None

    def new_request(self, **kwargs):
        """
        Create a new request with some parameters

        :param kwargs:
        :return: `RequestInitializer`
        """

        return self

    def execute(self, only_user_data=False):
        """
        Return a list or dict, dict states the last meta-data

        :return: a list or dict
        """
        pass


class JsonHandler:
    def __init__(self, **kwargs):
        """
        Initialization for json handler

        """
        pass

    def request_data(self):
        return self

    def _separate_raw_data(self, raw_data):
        """
        Separate raw `python-like` data to two parts

        :param raw_data: `dict`
        """
        for key, value in raw_data.items():
            if type(value) == dict:
                self.data_dict[key] = value
            elif type(value) == list:
                self.data_list[key] = value

    def retrieve(self, data_only_filter="all", return_type="python"):
        """
        Response will return data from your choice, you can choose different data\
        include two type: `python-like` data, `model-like` data, or choose data source: \
        `list-data`, `dict-data` or all data but divided two parts.

        :param data_only_filter: options: ("dict", "list", "all")
        :param return_type: options: ("json", "model")
        :return: a dict type data
        """
        if return_type == "python":
            if data_only_filter == "all":
                return dict(dict_data=self.data_dict, list_data=self.data_list)
            elif data_only_filter == "list":
                return self.data_list
            elif data_only_filter == "dict":
                return self.data_dict
            else:
                print(">>>> Data filter only: {'all', 'list', 'dict'}, your: %s" % data_only_filter)
                exit(1)
        elif return_type == "model":
            if data_only_filter == "all":
                return dict(dict_data=DictModel(name="obj_dict", raw_data=self.data_dict),
                            list_data=DictModel(name="obj_list", raw_data=self.data_list))
            elif data_only_filter == "list":
                return DictModel(name="obj_dict", raw_data=self.data_dict)
            elif data_only_filter == "dict":
                return DictModel(name="obj_list", raw_data=self.data_list)
            else:
                print(">>>> Data filter only: {'all', 'list', 'dict'}, your: %s" % data_only_filter)
                exit(1)
        else:
            print(">>>> Return type only: {'python', 'model'}, your: %s" % return_type)
            exit(1)
