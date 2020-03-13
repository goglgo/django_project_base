from django.db import models
from datetime import datetime
from django.utils import timezone
'''
# Flow 기술

## 1. 오더 받기
> Shipment_orderModel을 통해 각 서포트 타입별 오더를 받는다.
||| 엑셀 오더 형식이 이렇게 때문에 별 수 없다.
||| 오더 받는 형식에서 이걸 따따로 개별 명시해주어 데이터를 받아야 할 것 같다.

> Support_Spec은 각 사이즈별 오더를 가져올 모델이다.

> OrderSpecification

'''

class Support_Spec(models.Model):
    support_type    = models.CharField(max_length=20, verbose_name='규격')
    support_length  = models.IntegerField(verbose_name='길이')
    
    objects = models.Manager()

    def __str__(self):
        return f'{self.support_type} / {str(self.support_length)}'


class car_size(models.Model):
    car_size = models.CharField(max_length=10, verbose_name='차량종류')

    def __str__(self):
        return self.car_size


class DriverInformation(models.Model):
    car_no = models.CharField(max_length=10, verbose_name='차량번호')
    phone_number_field = models.CharField(max_length=15, verbose_name='전화번호')
    car_size = models.ForeignKey(car_size, on_delete=models.CASCADE, related_name='size')

    def __str__(self):
        return f"{self.car_size.car_size} / {self.car_no} / {self.phone_number_field}"


class LocationModel(models.Model):
    ERP_Number          =   models.CharField(max_length=30, verbose_name='공사번호')
    company_name    = models.CharField(max_length=20, verbose_name='업체명')
    location_name    = models.CharField(max_length=30, verbose_name='현장명')

    def __str__(self):
        return f"{self.company_name} / {self.location_name}"



# Create your models here.
class Shipment_orderModel(models.Model):
    submit_date     = models.DateField(verbose_name='접수일', auto_now=True)
    salesman_name   = models.CharField(max_length=10, verbose_name='영업사원')
    Location_fk     = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    district_name   = models.CharField(max_length=10, verbose_name='동')
    support_type    = models.ForeignKey(Support_Spec,on_delete=models.CASCADE, related_name='ship_order_type')
    is_it_head      = models.BooleanField(default=False, verbose_name='헤드유무')
    quantity        = models.IntegerField(default=0, verbose_name='수량')
    requst_arrival_option = models.CharField(default='당일착', verbose_name='도착도', max_length=10)
    other_notes     = models.TextField(verbose_name='기타사항', null=True, blank=True)
    location_info   = models.CharField(verbose_name='지역', max_length=20)
    
    objects = models.Manager()



class OrderSpecification(models.Model):
    # django.utils.timezone.now
    # submit_date = models.DateField(verbose_name='접수일', default=datetime.now())
    submit_date = models.DateField(verbose_name='접수일', default=timezone.now)
    order_status = models.CharField(verbose_name='오더상태', default='대기',
                                    max_length=20,) # 출하됨, 취소, 회차
    # 배차번호를 기준으로 땡기자.
    order_no    = models.IntegerField(verbose_name='배차번호',null=True, blank=True)
    quantity        = models.IntegerField(default=0, verbose_name='수량')
    support_type    = models.ForeignKey(Support_Spec, 
                                    on_delete=models.CASCADE, related_name='specific_type')
    driver_inormation = models.ForeignKey(DriverInformation, on_delete=models.CASCADE, blank=True, null=True)
    out_time = models.DateTimeField(auto_now_add=True, verbose_name='변동시간')

    objects = models.Manager()

    def __str__(self):
        return f'{self.order_no} / {self.support_type.support_type}-{self.support_type.support_length} / {self.quantity}'


