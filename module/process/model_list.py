class ListModel:
    def __init__(self, raw_data, name):
        """
        ListModel stores a `list` of meta-data, you can call a meta-data with: `get` method like:

        ```
        model = ListModel(raw_data=data, name=model_name)
        model.get(idx=4)
        ```

        if the `idx` larger than the size of data or lower than 0, `get` will return `None`

        :param raw_data: json data
        :param name: the name of this ListModel, often end with `s`, for example: `behaviors`
        """
        self.name = name + "s"
        self.data_list = []

        self._scan(raw_data)

    def __str__(self):
        return "<ListModel: %s" % self.name

    def _scan(self, raw_data_set):
        from model_dict import DictModel

        for item in raw_data_set:
            if type(item) == dict:
                self.data_list.append(DictModel(name=self.name, raw_data=item))
            else:
                self.data_list.append(item)
        self.size = len(self.data_list)

    def get(self, idx):
        return None if idx < 0 or idx > self.size else self.data_list[idx]

