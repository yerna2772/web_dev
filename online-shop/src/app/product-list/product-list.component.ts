import { Component, OnInit } from '@angular/core';
import { NgModule } from '@angular/core'
// import { products } from '../products'
import { ProductService } from '../product.service'
import { CategoryService } from '../category.service'
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  products: [] = [];
  categories: [] = [];
  category: number;
  // params: string;

  constructor(private productService: ProductService, private categoryService: CategoryService, private route: ActivatedRoute) { 
    this.getAllCategories();
    this.route.paramMap.subscribe(params => {
      this.category = this.categories[params.get('id')].id;
    })
   }

  ngOnInit(): void {
    // this.getAllProducts();
    if(this.category != undefined)
      this.getProductsByCategory(this.category);
    else
      this.getAllProducts();

    console.log(this.category)
    console.log(this.products)
    console.log('-------------')
  }

  getAllProducts() {
    this.productService.getProducts().subscribe(products => this.products = products)
  }

  getAllCategories() {
    this.categoryService.getAllCategories().subscribe(categories => this.categories = categories)
  }

  getProductsByCategory(id: number) {
    this.productService.getProductsByCategory(id).subscribe(products => this.products = products)
  }

}
