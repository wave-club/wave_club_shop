from django.shortcuts import render, redirect
from django.views.generic.base import View

from random import shuffle

# Create your views here.
from .models import Goods


class GoodsView(View):
    
    def post(self, request):
        userid = request.session.get('_auth_user_id')

        def getTotalStar(stars_list):
            return 1


        datas_list = list(range(1700))
        shuffle(datas_list)
        order_data = ','.join(str(v) for v in datas_list)

        goods = Goods()
        goods.userId = userid
        goods.name = request.POST.get('nick_name', '')
        goods.contact_action = request.POST.get('contact_action', '')
        goods.project_url = request.POST.get('project_url', '')
        goods.star_num = request.POST.get('star_num', 0)
        goods.follow_num = request.POST.get('follow_num', 0)
        goods.fork_num = request.POST.get('fork_num', 0)
        goods.watch_num = request.POST.get('watch_num', 0)
        goods.order_price = int(goods.star_num) * 1 + int(goods.follow_num) * 2 + int(goods.fork_num) * 2 + int(goods.watch_num) * 3
        goods.order_data = order_data


        goods.start_point = getTotalStar(1)


        goods.save()

        return redirect('/goodsList/')

    def get(self, request):
        return render(request, 'buy.html', {})
        

class PriceView(View):

    def get(self, request):
        return render(request, 'price_detail.html', {})

class GoodsListView(View):

    def get(self, request):
        userid = request.session.get('_auth_user_id')

        goods_list = Goods.objects.filter(userId=userid)
        print(goods_list)
        return render(request, 'goods_list.html', {
            'goods_list': goods_list
        })        
