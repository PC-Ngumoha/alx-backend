# Pagination

## Useful Points

- _Pagination_ is a technique used in the development of efficient APIs. It entails that the results of a query be split into pages so as to minimize the level of traffic required when trying to retrieve results. Thus, improving the Developer Experience or _DX_ in the process.

- Techniques for implementing pagination:
  - **Limit/Offset** pagination. Simplest form of pagination, mostly used when working with APIs built on a SQL database. Read about it's downsides [here](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#downsides-3)

  - **Keyset** pagination. Keyset pagination uses the filter values of the last page to fetch the next set of items. Those columns would be indexed. Read about it's downsides [here](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#downsides-4)

  **Seek** pagination. Seek Paging is an extension of Keyset paging. By adding an *after_id* or *start_id* URL parameter, we can remove the tight coupling of paging to filters and sorting. Read about it's downsides [here](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#downsides-5)

- _HATEOAS_ is an API/application operational constraint specific to _REST_ applications. In this, the client interacts with the network (server) which provides information dynamically through the use of hypermedia. A client therefore, needs little to no prior knowledge about how to interact with an app beyond a generic understanding of hypermedia.

- _HATEOAS_ essentially enables the client and server parts of an application to be developed and to evolve independently of one another.

- The phrase _Engine of Application State_ in _HATEOAS_ simply refers to the fact that actions that can be performed on a resource from the network vary with the state of the resource.

- A commonly used implementation of the _HATEOAS_ constraint is the _Hypertext Application Language_ or _HAL_. _HAL_ is a convention for defining hypermedia links to external resources within JSON and XML.




## Useful Links

- [Pagination Explanation](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)

- [HATEOAS (Hypermedia As The Engine of Application State)](https://en.wikipedia.org/wiki/HATEOAS)
