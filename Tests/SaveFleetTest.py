from datetime import timedelta

from Bot.SlackChannels import SlackChannels
from Commands.Commands import commands
from Core.BaseInfiniteTest import BaseInfiniteTest
from Enums.FleetMissionTypes import FleetMissionTypes
from Screens.OverviewScreen import OverviewScreen


class SaveFleetTest(BaseInfiniteTest):

    SAVE_FLEET_TIMEOUT = timedelta(minutes=10)

    def main_loop(self):
        print 'start loop'
        overview_screen = OverviewScreen()
        log = overview_screen.fleetAlertsTab.get_log()
        print 'log = '
        for el in log:
            print el.__str__()
        enemy_fleets = \
            filter(
                lambda el:
                el.is_friendly is False and
                el.mission_type == FleetMissionTypes.ATTACK and
                not el.is_return, log)
        for fleet in enemy_fleets:
            if fleet.remaining_time < self.SAVE_FLEET_TIMEOUT:
                self.slack_bot.send_message('we are under attack:\n{}'.format(fleet), channel=SlackChannels.ALERTS)
                commands.save_fleet(fleet.to_coordinates)
        commands.return_fleet()
        print 'end loop'


if __name__ == '__main__':
    test = SaveFleetTest()
    test()
