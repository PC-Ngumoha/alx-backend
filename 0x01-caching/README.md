# Caching

## Useful Points

- _Caching_ is a technique used to improve performance. It essentially involves placing recently or often used data in memory locations which are faster or computationally cheaper to access **_i.e. Memory locations which are nearer to where the data is supposed to be used._**

- In computer science, _Cache Replacement Policies_ or _Cache Replacement Algorithms_ are instructions which a computer program or hardware structure can optimally use to manage a cache of information.

- There are two primary factors to consider when evaluating a cache:
  - **Hit Ratio:** Describes how often an item is found when searched for.
  - **Latency:** Describes how long it takes a cache to return an item that was requested for when said item has been found.

- Every replacement policy is a compromise between _hit rate_ and _latency_.

- Some Cache Replacement Policies to know about include:
  - **First-In-First-Out or F.I.F.O:** The cache evicts blocks of information in the order in which they were added regardless of how often or how many times they were accessed before. This doesn't seem to be a very helpful policy because all items end up being evicted regardless of how often or recently they've been accessed simply because they've been in the cache for long enough.

  - **Last-In-First-Out or L.I.F.O:** The cache evicts the most recently added block first regardless of how often or how many times it was accessed.

  - **Least-Recently-Used or L.R.U:** The cache evicts the least recently used items/blocks first. This also entails that the cache must have a way of keep track of the usage frequency of each item.

  - **Most-Recently-Used or M.R.U:** The cache evicts the most recently used items/blocks first.

  - **Least-Frequently-Used or L.F.U:** The cache keeps track of how often items stored within it are accessed and evicts the items which are accessed less often. This has a problem that of an item is accessed excessively over a short period of time, it's going to be much harder to evict said item even when it has not been accessed for a longer time since then.

- Caches are limited by the fact that they can be polluted with useless junk that may never be used and this might end up costing us valuable cache memory. This is usually reduced by ensuring that items are not cached when they are first accessed by the user. But as they are accessed more and more, then they are cached. This not completely avoid the possibility of caching junk but it does help us minimize the chances of junk making it into the cache in the first place.

## Useful Links

- [Cache Replacement Policies (FIFO, LIFO, MRU, LRU & LFU)](https://en.wikipedia.org/wiki/Cache_replacement_policies)

- [Cache Replacement Algorithms (Simplified Explanation for LRU, FIFO & LFU)](https://dev.to/satrobit/cache-replacement-algorithms-how-to-efficiently-manage-the-cache-storage-2ne1)
