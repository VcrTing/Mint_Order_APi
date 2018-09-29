from locust import HttpLocust, TaskSet, task

# 要测的链接
url2 = 'http://39.107.96.126：8000/v1/goods'

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print('locust start')

    # 这里执行任务
    @task(1)
    def blm(self):
        # get 请求方式，请求 url2 链接
        self.client.get(url2)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://39.107.96.126：8000'
    min_wait = 500 # 最小等待
    max_wait = 800 # 最大等待
