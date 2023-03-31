#!/usr/bin/env python3
"""
API session db module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ Session DB Auth """

    def create_session(self, user_id: str = None) -> str:
        """  returns a Session ID and creates a UserSession record in DB if user_id is valid """
     
        if user_id is None or isinstance(user_id, str) is False:
            return None
        else:

            session_id = SessionExpAuth().create_session(user_id)
            if (self.user_id_for_session_id(session_id) is not None):
                return self.user_id_for_session_id(session_id)
            UserSession(user_id=user_id, session_id=session_id).save()
            return session_id


    def user_id_for_session_id(self, session_id: str = None) -> str:
        """  returns the User ID linked to a UserSession created before with """

        if session_id is None or isinstance(session_id, str) is False:
            return None
        else:
            return UserSession.search({'session_id': session_id}).first().user_id

    def destroy_session(self, request=None):
        """ Deletes user session to logout """
        pass
