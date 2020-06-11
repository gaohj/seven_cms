
class FromMixin(object):
    def get_errors(self):
        if hasattr(self,'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            #{'password': [{'message': '最短不能少于6个字符', 'code': 'min_length'}]}
            #{'password':['adf','haha']}
            for key,message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}

