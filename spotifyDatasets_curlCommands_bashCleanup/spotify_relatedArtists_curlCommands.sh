#!/bin/bash

token="BQCULOc0TEE_XTs5g0L6U5XPXRf0-vDloOuHlUFG7DBUeE77ag7hld8EnhsN8ct-XSw8h64NA76m7i8oamvBChJSyXbdR130yrKUNE-0KINtc7wUnndFXbyYHytvffxLVNVKe0zvdpLQOfE"
artistids=( 246dkjvS1zLTtiykXe5h60 7c0XG5cIJTrrAgEC3ULPiq 3TVXtAsR1Inumwj472S9r4 6LuN9FCkKOj5PcnpouEgny 2cWZOOzeOm4WmBJRnD5R7I 2qxJFvFYMEDqd7ui6kSAcq 6WY7D3jk8zTrHtmkqqo5GI 4lDBihdpMlOalxy1jkUbPl 2YZyLoL8N0Wb9xBt1NhZWg 1Xyo4u8uXC1ZmMpatF05PJ 7tYKF4w9nC0nq9CsPZTHyP 64KEffDW9EtZ1y2vBYgq8T 1zNqDE7qDGCsyzJwohVaoX 4GvEc3ANtPPjt1ZJllr5Zl 4WN5naL3ofxrVBgFpguzKo 4ScCswdRlyA23odg9thgIO 3JhNCzhSMTxs9WLGJJxWOY 2U3FuHYvL3vhkbDAXm24Ep 69GGBxA162lTqCwzJG5jLp 6M2wZ9GZgrQXHCFfjv46we 0LyfQWJT6nXafLPZqxe9Of 0ZED1XzwlLHW4ZaG4lOT6m 5p7f24Rk5HkUZsaS3BLG5F 1okJ4NC308qbtY9LyHn6DO 4nDoRrQiYLoBzwC5BhVJzF 6oMuImdp5ZcFhWP0ESe6mG 04gDigrS5kc9YWfZHwBETP 31W5EY0aAly4Qieq6OFu6I 4TEJudQY2pXxVHPE3gD2EU 31TPClRtHm23RisEBtV3X7 4YLtscXsxbVgi031ovDDdh 0du5cEVh5yTK9QJze8zA0C 4kYSro6naA4h99UJvo89HB 5pUo3fmmHT8bhCyHE52hA6 5CCwRZC6euC8Odo6y9X8jr 28ExwzUQsvgJooOI0X1mr3 1RyvyyTE3xzB2ZywiAwp0i 53KwLdlmrlCelAZMaLVZqU 5JZ7CnR6gTvEMKX4g70Amv 3qBKjEOanahMxlRojwCzhI 6s22t5Y3prQHyaHWUN1R1C 4LAz9VRX8Nat9kvIzgkg2v 7d3WFRME3vBY2cgoP38RDo 04ei5kNgmDuNAydFhhIHnD 64M6ah0SkkRsnPGtGiRAbb 3b8QkneNDz4JHKKKlLgYZg 2LZDXcxJWgsJfKXZv9a5eG 738wLrAtLtCtFOLvQBXOXp 738wLrAtLtCtFOLvQBXOXp 360IAlyVv4PCEVjgyMZrxK 0Y5tJX1MQlPlqiwlOH1tJY 02kJSzxNuaWGqwubyUba0Z 26VFTg2z8YR0cCuwLzESi2 1pPmIToKXyGdsCF6LmqLmI 7CajNmpbOovFoOoasH2HaY 14rP13jdQNgQvuPA2AkBgm 4VMYDCV2IEDYJArk749S6m 3EXdLajEO02ziZ90P90bSW 586uxXMyD5ObPuzjtrzO1Q 4j5KBTO4tk7up54ZirNGvK 2x7EATekOPhFGRx3syMGEC 0WuYfDB2hAYzybfAd75fvb 7dGJo4pcD2V6oG8kP0tJRR 6eUKZXaKkcviH0Ku9w2n3V 7HV2RI2qNug4EcQqLbCAKS 63nv0hWWDob56Rk8GlNpN8 4AVFqumd2ogHFlRbKIjp1t 4olE3I5QU0dvSR7LIpqTXc 07YZf4WDAMNwqr4jfgOZ8y 6vXTefBL93Dj5IqAWq6OTv 3mPc8WGusz2XF3Tvs3AKCR 5Rl15oVamLq7FbSb0NNBNy 3Isy6kedDrgPYoTS1dazA9 1Cs0zKBU1kc0i8ypK3B9ai 4obzFoKoKRHIphyHzJ35G3 60d24wfXkVzDSfLS6hyCjZ 4mHAu7NX2UNsnGXjviBD9e 0haZhu4fFKt0Ag94kZDiz2 07YZf4WDAMNwqr4jfgOZ8y 3EiLUeyEcA6fbRPSHkG5kb 4Q6nIcaBED8qUel8bBx6Cr 7hssUdpvtY5oiARaUDgFZ3 )

for id in "${artistids[@]}"
do
	curl -X "GET" "https://api.spotify.com/v1/artists/$id" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $token" >> spotify_relatedArtists_artistData_TodaysTopHits.txt
	curl -X "GET" "https://api.spotify.com/v1/artists/$id/related-artists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $token" >> spotify_relatedArtists_relatedArtistData_TodaysTopHits.txt
	echo -e "\n"$id >> spotify_relatedArtists_relatedArtistData_TodaysTopHits.txt
done
