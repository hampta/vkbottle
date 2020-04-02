# Generated with love
import typing
import enum
from vkbottle.types import responses
from .access import APIAccessibility
from .method import BaseMethod


class WallCloseComments(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.closeComments
        From Vk Docs: 
        Access from user, group token(s)
        :param owner_id: 
        :param post_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.closeComments", params)


class WallCreateComment(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(
        self,
        owner_id: int,
        post_id: int,
        from_group: int,
        message: str,
        reply_to_comment: int,
        attachments: typing.List,
        sticker_id: int,
        guid: str,
    ):
        """ wall.createComment
        From Vk Docs: Adds a comment to a post on a user wall or community wall.
        Access from user, group token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param from_group: Group ID.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param reply_to_comment: ID of comment to reply.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media ojbect: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. For example: "photo100172_166443618,photo66748_265827614"
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.createComment", params)


class WallDelete(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.delete
        From Vk Docs: Deletes a post from a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be deleted.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.delete", params)


class WallDeleteComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int):
        """ wall.deleteComment
        From Vk Docs: Deletes a comment on a post on a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: Comment ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.deleteComment", params)


class WallEdit(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        post_id: int,
        friends_only: bool,
        message: str,
        attachments: typing.List,
        services: str,
        signed: bool,
        publish_date: int,
        lat: typing.Any,
        long: typing.Any,
        place_id: int,
        mark_as_ads: bool,
        close_comments: bool,
        poster_bkg_id: int,
        poster_bkg_owner_id: int,
        poster_bkg_access_hash: str,
    ):
        """ wall.edit
        From Vk Docs: Edits a post on a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: 
        :param friends_only: 
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error is thrown."
        :param services: 
        :param signed: 
        :param publish_date: 
        :param lat: 
        :param long: 
        :param place_id: 
        :param mark_as_ads: 
        :param close_comments: 
        :param poster_bkg_id: 
        :param poster_bkg_owner_id: 
        :param poster_bkg_access_hash: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.edit", params)


class WallEditAdsStealth(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        post_id: int,
        message: str,
        attachments: typing.List,
        signed: bool,
        lat: typing.Any,
        long: typing.Any,
        place_id: int,
        link_button: str,
        link_title: str,
        link_image: str,
        link_video: str,
    ):
        """ wall.editAdsStealth
        From Vk Docs: Allows to edit hidden post.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.editAdsStealth", params)


class WallEditComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self, owner_id: int, comment_id: int, message: str, attachments: typing.List
    ):
        """ wall.editComment
        From Vk Docs: Edits a comment on a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: Comment ID.
        :param message: New comment text.
        :param attachments: List of objects attached to the comment, in the following format: , "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media attachment owner. '<media_id>' — Media attachment ID. For example: "photo100172_166443618,photo66748_265827614"
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.editComment", params)


class WallGet(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        owner_id: int,
        domain: str,
        offset: int,
        count: int,
        filter: str,
        extended: bool,
        fields: typing.List,
    ):
        """ wall.get
        From Vk Docs: Returns a list of posts on a user wall or community wall.
        Access from user, service token(s)
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param domain: User or community short address.
        :param offset: Offset needed to return a specific subset of posts.
        :param count: Number of posts to return (maximum 100).
        :param filter: Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall
        :param extended: '1' — to return 'wall', 'profiles', and 'groups' fields, '0' — to return no additional fields (default)
        :param fields: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.get", params)


class WallGetById(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        posts: typing.List,
        extended: bool,
        copy_history_depth: int,
        fields: typing.List,
    ):
        """ wall.getById
        From Vk Docs: Returns a list of posts from user or community walls by their IDs.
        Access from user, service token(s)
        :param posts: User or community IDs and post IDs, separated by underscores. Use a negative value to designate a community ID. Example: "93388_21539,93388_20904,2943_4276,-1_1"
        :param extended: '1' — to return user and community objects needed to display posts, '0' — no additional fields are returned (default)
        :param copy_history_depth: Sets the number of parent elements to include in the array 'copy_history' that is returned if the post is a repost from another wall.
        :param fields: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.getById", params)


class WallGetComments(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        owner_id: int,
        post_id: int,
        need_likes: bool,
        start_comment_id: int,
        offset: int,
        count: int,
        sort: str,
        preview_length: int,
        extended: bool,
        fields: typing.List,
        comment_id: int,
        thread_items_count: int,
    ):
        """ wall.getComments
        From Vk Docs: Returns a list of comments on a post on a user wall or community wall.
        Access from user, service token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id: 
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return (maximum 100).
        :param sort: Sort order: 'asc' — chronological, 'desc' — reverse chronological
        :param preview_length: Number of characters at which to truncate comments when previewed. By default, '90'. Specify '0' if you do not want to truncate comments.
        :param extended: 
        :param fields: 
        :param comment_id: Comment ID.
        :param thread_items_count: Count items in threads.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.getComments", params)


class WallGetReposts(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(self, owner_id: int, post_id: int, offset: int, count: int):
        """ wall.getReposts
        From Vk Docs: Returns information about reposts of a post on user wall or community wall.
        Access from user, service token(s)
        :param owner_id: User ID or community ID. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        :param offset: Offset needed to return a specific subset of reposts.
        :param count: Number of reposts to return.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.getReposts", params)


class WallOpenComments(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.GROUP,
    ]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.openComments
        From Vk Docs: 
        Access from user, group token(s)
        :param owner_id: 
        :param post_id: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.openComments", params)


class WallPin(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.pin
        From Vk Docs: Pins the post on wall.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.pin", params)


class WallPost(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        friends_only: bool,
        from_group: bool,
        message: str,
        attachments: typing.List,
        services: str,
        signed: bool,
        publish_date: int,
        lat: typing.Any,
        long: typing.Any,
        place_id: int,
        post_id: int,
        guid: str,
        mark_as_ads: bool,
        close_comments: bool,
        mute_notifications: bool,
    ):
        """ wall.post
        From Vk Docs: Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param friends_only: '1' — post will be available to friends only, '0' — post will be available to all users (default)
        :param from_group: For a community: '1' — post will be published by the community, '0' — post will be published by the user (default)
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param services: List of services or websites the update will be exported to, if the user has so requested. Sample values: 'twitter', 'facebook'.
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param publish_date: Publication date (in Unix time). If used, posting will be delayed until the set time.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param post_id: Post ID. Used for publishing of scheduled and suggested posts.
        :param guid: 
        :param mark_as_ads: 
        :param close_comments: 
        :param mute_notifications: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.post", params)


class WallPostAdsStealth(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        owner_id: int,
        message: str,
        attachments: typing.List,
        signed: bool,
        lat: typing.Any,
        long: typing.Any,
        place_id: int,
        guid: str,
        link_button: str,
        link_title: str,
        link_image: str,
        link_video: str,
    ):
        """ wall.postAdsStealth
        From Vk Docs: Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param message: (Required if 'attachments' is not set.) Text of the post.
        :param attachments: (Required if 'message' is not set.) List of objects attached to the post, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'page' — wiki-page, 'note' — note, 'poll' — poll, 'album' — photo album, '<owner_id>' — ID of the media application owner. '<media_id>' — Media application ID. Example: "photo100172_166443618,photo66748_265827614", May contain a link to an external page to include in the post. Example: "photo66748_265827614,http://habrahabr.ru", "NOTE: If more than one link is being attached, an error will be thrown."
        :param signed: Only for posts in communities with 'from_group' set to '1': '1' — post will be signed with the name of the posting user, '0' — post will not be signed (default)
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param place_id: ID of the location where the user was tagged.
        :param guid: Unique identifier to avoid duplication the same post.
        :param link_button: Link button ID
        :param link_title: Link title
        :param link_image: Link image url
        :param link_video: Link video ID in format "<owner_id>_<media_id>"
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.postAdsStealth", params)


class WallReportComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int, reason: int):
        """ wall.reportComment
        From Vk Docs: Reports (submits a complaint about) a comment on a post on a user wall or community wall.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the wall.
        :param comment_id: Comment ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.reportComment", params)


class WallReportPost(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, post_id: int, reason: int):
        """ wall.reportPost
        From Vk Docs: Reports (submits a complaint about) a post on a user wall or community wall.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the wall.
        :param post_id: Post ID.
        :param reason: Reason for the complaint: '0' – spam, '1' – child pornography, '2' – extremism, '3' – violence, '4' – drug propaganda, '5' – adult material, '6' – insult, abuse
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.reportPost", params)


class WallRepost(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(
        self,
        object: str,
        message: str,
        group_id: int,
        mark_as_ads: bool,
        mute_notifications: bool,
    ):
        """ wall.repost
        From Vk Docs: Reposts (copies) an object to a user wall or community wall.
        Access from user token(s)
        :param object: ID of the object to be reposted on the wall. Example: "wall66748_3675"
        :param message: Comment to be added along with the reposted object.
        :param group_id: Target community ID when reposting to a community.
        :param mark_as_ads: 
        :param mute_notifications: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.repost", params)


class WallRestore(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.restore
        From Vk Docs: Restores a post deleted from a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID from whose wall the post was deleted. Use a negative value to designate a community ID.
        :param post_id: ID of the post to be restored.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.restore", params)


class WallRestoreComment(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, comment_id: int):
        """ wall.restoreComment
        From Vk Docs: Restores a comment deleted from a user wall or community wall.
        Access from user token(s)
        :param owner_id: User ID or community ID. Use a negative value to designate a community ID.
        :param comment_id: Comment ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.restoreComment", params)


class WallSearch(BaseMethod):
    access_token_type: APIAccessibility = [
        APIAccessibility.USER,
        APIAccessibility.SERVICE,
    ]

    async def __call__(
        self,
        owner_id: int,
        domain: str,
        query: str,
        owners_only: bool,
        count: int,
        offset: int,
        extended: bool,
        fields: typing.List,
    ):
        """ wall.search
        From Vk Docs: Allows to search posts on user or community walls.
        Access from user, service token(s)
        :param owner_id: user or community id. "Remember that for a community 'owner_id' must be negative."
        :param domain: user or community screen name.
        :param query: search query string.
        :param owners_only: '1' – returns only page owner's posts.
        :param count: count of posts to return.
        :param offset: Offset needed to return a specific subset of posts.
        :param extended: show extended post info.
        :param fields: 
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.search", params)


class WallUnpin(BaseMethod):
    access_token_type: APIAccessibility = [APIAccessibility.USER]

    async def __call__(self, owner_id: int, post_id: int):
        """ wall.unpin
        From Vk Docs: Unpins the post on wall.
        Access from user token(s)
        :param owner_id: ID of the user or community that owns the wall. By default, current user ID. Use a negative value to designate a community ID.
        :param post_id: Post ID.
        """

        params = {k: v for k, v in locals().items() if k not in ["self"]}
        return await self.request("wall.unpin", params)


class Wall:
    def __init__(self, request):
        self.close_comments = WallCloseComments(request)
        self.create_comment = WallCreateComment(request)
        self.delete = WallDelete(request)
        self.delete_comment = WallDeleteComment(request)
        self.edit = WallEdit(request)
        self.edit_ads_stealth = WallEditAdsStealth(request)
        self.edit_comment = WallEditComment(request)
        self.get = WallGet(request)
        self.get_by_id = WallGetById(request)
        self.get_comments = WallGetComments(request)
        self.get_reposts = WallGetReposts(request)
        self.open_comments = WallOpenComments(request)
        self.pin = WallPin(request)
        self.post = WallPost(request)
        self.post_ads_stealth = WallPostAdsStealth(request)
        self.report_comment = WallReportComment(request)
        self.report_post = WallReportPost(request)
        self.repost = WallRepost(request)
        self.restore = WallRestore(request)
        self.restore_comment = WallRestoreComment(request)
        self.search = WallSearch(request)
        self.unpin = WallUnpin(request)