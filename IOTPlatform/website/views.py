from django.http import JsonResponse
# from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser
from website import database
from website.console import send

error_msg = {'code': 100, 'message': 'request parameter error'}


class Login(APIView):
    parser_classes = [JSONParser, FormParser]
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        res = database.login(username, password)
        return JsonResponse(res)


class Register(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        res = database.register(username, password, email)
        return JsonResponse(res)


class Dashboard(APIView):
    def get(self, request):
        res = database.dashboard(request.user, None, None)
        return JsonResponse(res)


class Chart(APIView):
    def get(self, request):
        res = database.charts(request.user, None, None)
        return JsonResponse(res)


class Device(APIView):
    parser_classes = [JSONParser, FormParser]

    def get(self, request):
        """获取设备"""
        res = database.get_device(request.user)
        return JsonResponse(res)

    def post(self, request):
        """新建设备"""
        name = request.data.get('name', None)
        introduce = request.data.get('introduce', None)
        tag = request.data.get('tag', None)
        # print(name,introduce,tag)
        res = database.add_device(request.user, name, introduce, tag)

        return JsonResponse(res)

    def put(self, request):
        """修改设备信息"""
        id = request.data.get('id', None)
        name = request.data.get('name', None)
        introduce = request.data.get('introduce', None)
        tag = request.data.get('tag', None)
        res = database.update_device(request.user, id, name, introduce, tag)
        return JsonResponse(res)

    def delete(self, request):
        id = request.data.get('id', None)
        apiKey = request.data.get('apiKey', None)
        res = database.del_device(request.user, id, apiKey)
        return JsonResponse(res)


class Stream(APIView):
    parser_classes = [JSONParser, FormParser]

    def get(self, request):
        """获取设备"""
        res = database.get_stream(request.user)
        return JsonResponse(res)

    def post(self, request):
        """
        新建数据流
        :param request: name, dev_id, qos, min 都不能为空
        :return:
        """
        name = request.data.get('name', None)
        unit = request.data.get('unit', None)
        unit_symbol = request.data.get('unit_symbol', None)
        qos = request.data.get('qos', 0)
        dev_id = request.data.get('dev_id', None)
        max = request.data.get('max', 0)
        min = request.data.get('min', 0)
        if not dev_id or not name:
            return JsonResponse(error_msg)
        if qos not in [0, 1, 2, '0', '1', '2'] or \
           min not in [0, 1, 2, 3, 4, 5, 6, 7, '0', '1', '2', '3', '4', '5', '6','7']:
            return JsonResponse(error_msg)
        res = database.add_stream(request.user, dev_id, name, unit, unit_symbol, max, min, qos)
        return JsonResponse(res)

    def put(self, request):
        """修改数据流信息"""
        device_id = request.data.get('dev_id', None)
        name = request.data.get('name', None)
        unit = request.data.get('unit', None)
        unit_symbol = request.data.get('unit_symbol', None)
        max = request.data.get('max', None)
        min = request.data.get('min', None)
        qos = request.data.get('qos', None)
        if not device_id or not name:
            return JsonResponse(error_msg)
        if qos not in [0, 1, 2, '0', '1', '2'] or \
           min not in [0, 1, 2, 3, 4, 5, 6, 7, '0', '1', '2', '3', '4', '5', '6','7']:
            return JsonResponse(error_msg)
        res = database.update_stream(request.user, device_id, name, unit, unit_symbol, max, min, qos)
        return JsonResponse(res)

    def delete(self, request):
        dev_id = request.data.get('dev_id', None)
        name = request.data.get('name', None)
        res = database.del_stream(request.user, dev_id, name)
        return JsonResponse(res)


class Console(APIView):
    parser_classes = [JSONParser, FormParser]

    def post(self, request):
        topic = request.data.get('topic')
        # topic 为必要参数必须要有
        if not topic:
            return JsonResponse(error_msg)
        # 此项参数允许为空
        payload = request.data.get('payload', None)
        qos = request.data.get('qos')
        # qos 参数只能为列表中的几个，否则无效
        if qos not in ['0', '1', '2', 1, 2, 0]:
            return JsonResponse(error_msg)
        data = {'topic': topic, 'payload': payload, 'qos': int(qos)}
        res = send(data)
        return JsonResponse(res)


class Trigger(APIView):
    parser_classes = [JSONParser, FormParser]

    def get(self, request):
        res = database.get_trigger(request.user)
        print(res)
        return JsonResponse(res)
