# Grapic-Price

다나와 그래픽카드 가격 스크래퍼

## How to use
1. danawa uri에서 pcode 부분을 추출합니다
    ```
    uri: http://prod.danawa.com/info/?pcode=14444705&keyword=asus+tuf+3070ti&cate=112753
    pcode -> 14444705
    ```
1. Danawa class instance를 생성할 때 생성자로 pcode를 전달합니다.
    ```python
    asus_rog_3070ti = Danawa(14444267)
    ```
1. `.script()` 메소드는 해당 pcode 제품에 대해 스크래핑을 진행합니다.
    ```python
    asus_rog_3070ti.scrap()
    ```
1. `.prices` attribute에 스크래핑 결과가 저장됩니다. 또는, `.pprint()` 메소드를 호출해서 출력할 수도 있습니다.
    ```python
    asus_rog_3070ti.pprint()
    ```

## Example
```python
from scrap import Danawa

if __name__ == '__main__':
    asus_tuf_3070ti = Danawa(14444705)
    asus_tuf_3070ti.scrap()
    asus_tuf_3070ti.pprint()

    asus_rog_3070ti = Danawa(14444267)
    asus_rog_3070ti.scrap()
    asus_rog_3070ti.pprint()
```

<img width="399" alt="image" src="https://user-images.githubusercontent.com/8157830/163780351-994661b1-ad2d-4b6f-967f-6f3ed4f692ec.png">

## 여담
* 그래픽 카드 외 다른 상품에도 동작합니다

## License
* MIT License