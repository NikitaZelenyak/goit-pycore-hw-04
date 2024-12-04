def get_cats_info(data):
    cuts_info= []
    for cut in data:
        id,name,year = cut.replace("\n", "").split(",")
        cuts_info.append({"id":id, "name":name, "year":year})
    return cuts_info