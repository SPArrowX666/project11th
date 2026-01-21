from django.db import models
from django.utils import timezone

class TrainingRecord(models.Model):
    TRAINING_TYPES = [
        ('drill', '基礎'),
        ('match', '試合'),
        ('footwork', 'フットワーク'),
        ('gym', '筋トレ'),
    ]
    
    FEELING_TYPES = [
        ('great', '好調'),
        ('good', '普通'),
        ('tired', '疲れた'),
        ('pain', '痛みあり'),
    ]

    # 字段定义
    date = models.DateField(default=timezone.now, verbose_name="練習日")
    training_type = models.CharField(max_length=20, choices=TRAINING_TYPES, verbose_name="メニュー")
    duration = models.IntegerField(help_text="分", verbose_name="練習時間(分)")
    feeling = models.CharField(max_length=20, choices=FEELING_TYPES, default='good', verbose_name="コンディション")
    memo = models.TextField(blank=True, verbose_name="練習メモ/反省点")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_training_type_display()} - {self.date}"