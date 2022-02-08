def findMedianSortedArrays(nums1, nums2):
    # ko skupno dolzino celostevilsko delimo z 2 dobimo
    # koliko mora biti elementov na levi in desni particiji
    skupna_dolzina = len(nums1) + len(nums2)
    dolzina_particije = skupna_dolzina // 2

    # zamenjamo, tako da je nums1 krajsa tabela
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    # delamo binary-search po nums1 (krajsi tabeli)
    # l indeks levi, r indeks desni
    l = 0
    r = len(nums1) - 1

    while True:
        sredina = (l + r) // 2
        # -2, ker gledamo indeks
        r_2 = dolzina_particije - sredina - 2

        # pogledamo ali te vrednosti ustrezajo
        a_l = nums1[sredina] if sredina >= 0 else float("-infinity")
        a_r = nums1[sredina + 1] if (sredina + 1) < len(nums1) else float("infinity")
        b_l = nums2[r_2] if r_2 >= 0 else float("-infinity")
        b_r = nums2[r_2 + 1] if (r_2 + 1) < len(nums2) else float("infinity")

        # to je okej
        if a_l <= b_r and b_l <= a_r:
            if skupna_dolzina % 2 == 1:
                return min(a_r, b_r)
            return (min(b_r, a_r) + max(b_l, a_l)) / 2
        elif a_l > b_r:
            r = sredina - 1
        else:
            l = sredina + 1


nums1 = [1, 2]
nums2 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))
