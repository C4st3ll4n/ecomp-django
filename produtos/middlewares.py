def my_mid(get_response):
    def middleware(request):
        print('hello middleware')
        if request.method == "GET":
            print('get middleware')

        response = get_response(request)
        print('goodbye middleware')
        return response

    return middleware
