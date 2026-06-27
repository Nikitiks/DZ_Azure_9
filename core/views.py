from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Product
from .forms import ProductForm
from .storage import upload_image

# tag_seed()
# category_seed()
class ProductListView(ListView):
    model = Product
    template_name ='product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.select_related('category').prefetch_related('tags').order_by('name')
    
class ProductCreateView(CreateView):
    model=Product
    form_class=ProductForm
    template_name='product_create.html'
    success_url=reverse_lazy('product-list')

    def from_valid(self, form):
        product = form.save(commit=False)

        image_file = self.request.FILES.get('images')
        if image_file:
            product.image_path = upload_image(image_file)

        product.save()
        return super().form_valid(form)