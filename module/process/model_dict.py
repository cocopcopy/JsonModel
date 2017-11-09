class DictModel:
    def __init__(self, raw_data, name):
        """
        DictModel stores a `dict` meta-data, you can call a meta-data with: `get` method like:

        ```
        model = DictModel(raw_data=data, name=name)
        mode.get("keyName")
        ```

        if has not this key, `get` will return `None`

        :param raw_data: json data
        :param name: the name of this DictModel
        """
        self.name = name
        self.data_set = dict()

        self._scan(raw_data)

    def __str__(self):
        return "<DictModel: %s>" % self.name

    def _scan(self, raw_data_set):
        from model_list import ListModel

        for key, value in raw_data_set.items():
            if type(value) == list:
                self.data_set[key] = ListModel(name=key + "s", raw_data=value)
            else:
                self.data_set[key] = value

    def get(self, key):
        return None if self.data_set.get(key) is None else self.data_set[key]

