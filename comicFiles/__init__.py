"""
    New idea: find orphaned files!
    
    That way, once everything is linked as it can be (yay manual review...) all that's left is the stuff that's not cared about!
"""



"""
    In case this ever needs updating again
    
    from django.contrib.auth.models import User
    from issues.models import Comic
    from comicFiles.models import ComicReadAndOwn

    owned = Comic.objects.filter(own=True)
    user = User.objects.get(pk=1)

    for issue in owned:
        print("{} :: {} - {}".format(issue.series.name, issue.number, issue.id))
        try:
            c = ComicReadAndOwn.objects.get(user=1, issue=issue.id)
        except:
            c = ComicReadAndOwn()
        c.issue = issue
        c.own = issue.own
        c.read = issue.read
        c.user = user
        c.save()
"""