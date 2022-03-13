import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { products } from './products';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() {

  }

  getProductById(id: number): Observable<any> {
    return of(products.find(product => product.id === id));
  }

  getProducts(): Observable<any> {
    return of(products);
  }

  getProductsByCategory(id: number): Observable<any> {
    let temp: any = [];
    products.forEach(item => {
      if(item.category_id === id)
        temp.push(item);
    })
    console.log('temp:', temp)
    return of(temp);
  }
}
